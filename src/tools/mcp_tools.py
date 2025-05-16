"""
MCP tool definitions for Simple Calculator MCP.
This file contains all the tool functions that are registered with the MCP server.
"""
import math
import logging
from typing import List, Dict, Any, Optional
from mcp.server.fastmcp import Context, FastMCP

logger = logging.getLogger("calculator-mcp")

def register_all_tools(mcp: FastMCP):
    """Register all tools with the MCP server"""
    
    @mcp.tool()
    async def add(a: float, b: float, ctx: Context = None) -> str:
        """
        Add two numbers together.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The sum of the two numbers with calculation details
        """
        logger.info(f"Calculating addition: {a} + {b}")
        result = a + b
        return format_result("Addition", a, b, result, "+")

    @mcp.tool()
    async def subtract(a: float, b: float, ctx: Context = None) -> str:
        """
        Subtract the second number from the first.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The difference between the two numbers with calculation details
        """
        logger.info(f"Calculating subtraction: {a} - {b}")
        result = a - b
        return format_result("Subtraction", a, b, result, "-")

    @mcp.tool()
    async def multiply(a: float, b: float, ctx: Context = None) -> str:
        """
        Multiply two numbers together.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The product of the two numbers with calculation details
        """
        logger.info(f"Calculating multiplication: {a} × {b}")
        result = a * b
        return format_result("Multiplication", a, b, result, "×")

    @mcp.tool()
    async def divide(a: float, b: float, ctx: Context = None) -> str:
        """
        Divide the first number by the second.
        
        Args:
            a: First number (dividend)
            b: Second number (divisor)
            
        Returns:
            The quotient of the division with calculation details
        """
        logger.info(f"Calculating division: {a} ÷ {b}")
        if b == 0:
            logger.warning("Division by zero attempted")
            return "Error: Division by zero is not allowed."
        
        result = a / b
        return format_result("Division", a, b, result, "÷")

    @mcp.tool()
    async def power(base: float, exponent: float, ctx: Context = None) -> str:
        """
        Raise the base to the power of the exponent.
        
        Args:
            base: The base number
            exponent: The exponent
            
        Returns:
            The result of the exponentiation with calculation details
        """
        logger.info(f"Calculating power: {base}^{exponent}")
        try:
            result = base ** exponent
            return format_result("Power", base, exponent, result, "^")
        except OverflowError:
            logger.warning(f"Overflow error in power calculation: {base}^{exponent}")
            return "Error: Result too large to compute."

    @mcp.tool()
    async def modulo(a: float, b: float, ctx: Context = None) -> str:
        """
        Calculate the remainder when the first number is divided by the second.
        
        Args:
            a: First number (dividend)
            b: Second number (divisor)
            
        Returns:
            The remainder of the division with calculation details
        """
        logger.info(f"Calculating modulo: {a} % {b}")
        if b == 0:
            logger.warning("Modulo by zero attempted")
            return "Error: Modulo by zero is not allowed."
        
        result = a % b
        return format_result("Modulo", a, b, result, "%")

    @mcp.tool()
    async def calculate(expression: str, ctx: Context = None) -> str:
        """
        Evaluate a simple mathematical expression.
        
        Args:
            expression: A mathematical expression as a string (e.g., "2 + 3 * 4")
            
        Returns:
            The result of the expression with calculation details
        
        Note: This function uses Python's eval() which can be dangerous with untrusted input.
        In a production environment, you should use a safer expression evaluator.
        """
        logger.info(f"Calculating expression: {expression}")
        try:
            # Whitelist allowed characters for basic safety
            allowed_chars = set("0123456789+-*/() .")
            if not all(c in allowed_chars for c in expression):
                logger.warning(f"Invalid characters in expression: {expression}")
                return "Error: Expression contains invalid characters. Only numbers and basic operators (+, -, *, /) are allowed."
            
            result = eval(expression)
            return f"## Calculation Result\n\n{expression} = {result}"
        except Exception as e:
            logger.error(f"Error evaluating expression: {expression}, error: {str(e)}")
            return f"Error evaluating expression: {str(e)}"

    @mcp.tool()
    async def square_root(number: float, ctx: Context = None) -> str:
        """
        Calculate the square root of a number.
        
        Args:
            number: The number to find the square root of
            
        Returns:
            The square root of the number with calculation details
        """
        logger.info(f"Calculating square root of {number}")
        if number < 0:
            logger.warning(f"Square root of negative number attempted: {number}")
            return "Error: Cannot calculate square root of a negative number."
        
        result = math.sqrt(number)
        return f"## Square Root Result\n\n√{number} = {result}"

    @mcp.tool()
    async def factorial(number: int, ctx: Context = None) -> str:
        """
        Calculate the factorial of a non-negative integer.
        
        Args:
            number: The non-negative integer to find the factorial of
            
        Returns:
            The factorial of the number with calculation details
        """
        logger.info(f"Calculating factorial of {number}")
        if not isinstance(number, int) or number < 0:
            logger.warning(f"Invalid factorial input: {number}")
            return "Error: Factorial is only defined for non-negative integers."
        
        if number > 170:
            logger.warning(f"Factorial too large: {number}")
            return "Error: Input too large, would cause overflow."
        
        try:
            result = math.factorial(number)
            return f"## Factorial Result\n\n{number}! = {result}"
        except Exception as e:
            logger.error(f"Error calculating factorial: {number}, error: {str(e)}")
            return f"Error calculating factorial: {str(e)}"

    @mcp.tool()
    async def logarithm(number: float, base: float = 10, ctx: Context = None) -> str:
        """
        Calculate the logarithm of a number with the specified base.
        
        Args:
            number: The number to find the logarithm of
            base: The base of the logarithm (default: 10)
            
        Returns:
            The logarithm result with calculation details
        """
        logger.info(f"Calculating logarithm: log_{base}({number})")
        if number <= 0:
            logger.warning(f"Logarithm of non-positive number attempted: {number}")
            return "Error: Cannot calculate logarithm of a non-positive number."
        
        if base <= 0 or base == 1:
            logger.warning(f"Invalid logarithm base: {base}")
            return "Error: Logarithm base must be positive and not equal to 1."
        
        try:
            result = math.log(number, base)
            return f"## Logarithm Result\n\nlog_{base}({number}) = {result}"
        except Exception as e:
            logger.error(f"Error calculating logarithm: log_{base}({number}), error: {str(e)}")
            return f"Error calculating logarithm: {str(e)}"

    @mcp.tool()
    async def trigonometric(function: str, angle: float, is_radians: bool = True, ctx: Context = None) -> str:
        """
        Calculate trigonometric functions (sin, cos, tan).
        
        Args:
            function: The trigonometric function to use ('sin', 'cos', 'tan')
            angle: The angle value
            is_radians: Whether the angle is in radians (True) or degrees (False)
            
        Returns:
            The trigonometric function result with calculation details
        """
        logger.info(f"Calculating {function}({angle}) {'radians' if is_radians else 'degrees'}")
        
        # Convert to lowercase for case-insensitive comparison
        function = function.lower()
        
        # Validate function name
        if function not in ['sin', 'cos', 'tan']:
            logger.warning(f"Invalid trigonometric function: {function}")
            return "Error: Function must be 'sin', 'cos', or 'tan'."
        
        # Convert degrees to radians if necessary
        if not is_radians:
            angle_rad = math.radians(angle)
            angle_display = f"{angle}°"
        else:
            angle_rad = angle
            angle_display = f"{angle} rad"
        
        try:
            # Calculate the result based on the function
            if function == 'sin':
                result = math.sin(angle_rad)
                func_name = "Sine"
            elif function == 'cos':
                result = math.cos(angle_rad)
                func_name = "Cosine"
            else:  # tan
                # Check for undefined values (multiples of π/2)
                if abs(math.cos(angle_rad)) < 1e-10:
                    logger.warning(f"Tangent undefined at {angle}")
                    return f"Error: Tangent is undefined at {angle_display} (multiple of π/2)."
                result = math.tan(angle_rad)
                func_name = "Tangent"
            
            return f"## {func_name} Result\n\n{function}({angle_display}) = {result}"
        except Exception as e:
            logger.error(f"Error calculating {function}: {angle}, error: {str(e)}")
            return f"Error calculating {function}: {str(e)}"

    @mcp.tool()
    async def health_check(ctx: Context = None) -> str:
        """
        Check if the server is running and responsive.
        
        Returns:
            A message indicating the server is healthy
        """
        logger.info("Health check requested")
        return "Simple Calculator MCP server is running and healthy!"

def format_result(operation, a, b, result, operator):
    """Format the calculation result in a consistent way"""
    return f"## {operation} Result\n\n{a} {operator} {b} = {result}"
