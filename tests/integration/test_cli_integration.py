import subprocess
import sys
import pytest


class TestCLIIntegration:
    """Test CLI application integrating with
    calculator module"""

    def run_cli(self, *args):
        """Helper method to run CLI and capture
        output"""
        cmd = [sys.executable, "src/cli.py"] + list(args)
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=".")
        return result

    def test_cli_add_integration(self):
        """Test CLI can perform addition"""
        result = self.run_cli("add", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "8"

    def test_cli_subtract_integration(self):
        """Test CLI can perform subtraction"""
        result = self.run_cli("subtract", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "2"

    def test_cli_multiply_integration(self): 
        """Test CLI can perform multiplication""" 
        result = self.run_cli("multiply", "5", "3") 
        assert result.returncode == 0 
        assert result.stdout.strip() == "15" 
     
    def test_cli_divide_integration(self): 
        """Test CLI can perform division""" 
        result = self.run_cli("divide", "5", "3") 
        assert result.returncode == 0 
        assert result.stdout.strip() == "1.67"

    def test_cli_subtract_missing_operand_error(self):
        """Test CLI handles missing operand for
        subtraction gracefully"""
        # call subtract with only one operand; CLI should exit with non-zero and print an error
        result = self.run_cli("subtract", "5")
        assert result.returncode == 1
        # CLI prints a generic unexpected error message for this case
        assert result.stdout.strip().startswith("Unexpected error:")

    def test_cli_sqrt_integration(self): 
        """Test CLI can perform square root""" 
        result = self.run_cli('sqrt', '16') 
        assert result.returncode == 0 
        assert result.stdout.strip() == '4' 
     
    def test_cli_error_handling_integration(self): 
        """Test CLI properly handles calculator errors""" 
        result = self.run_cli('divide', '10', '0') 
        assert result.returncode == 1 
        assert 'Cannot divide by zero' in result.stdout 
     
    def test_cli_invalid_operation_integration(self): 
        """Test CLI handles invalid operations""" 
        result = self.run_cli('invalid', '1', '2') 
        assert result.returncode == 1 
        assert 'Unknown operation' in result.stdout 
 
class TestCalculatorModuleIntegration: 
    """Test calculator module functions work together""" 
     
    def test_chained_operations(self): 
        """Test using results from one operation in another""" 
        from src.calculator import add, multiply, divide 
         
        # Calculate (5 + 3) * 2 / 4 
        step1 = add(5, 3)           # 8 
        step2 = multiply(step1, 2)   # 16   
        step3 = divide(step2, 4)     # 4 
         
        assert step3 == 4.0 
     
    def test_complex_calculation_integration(self): 
        """Test complex calculation using multiple functions""" 
        from src.calculator import power, square_root, add 
         
        # Calculate sqrt(3^2 + 4^2) = 5 (Pythagorean theorem) 
        a_squared = power(3, 2)      # 9 
        b_squared = power(4, 2)      # 16 
        sum_squares = add(a_squared, b_squared)  # 25 
        hypotenuse = square_root(sum_squares)    # 5 
        assert hypotenuse == 5.0 