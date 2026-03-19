# Numpy funtions
# https://www.hackerrank.com/challenges/np-arrays/problem
# https://www.hackerrank.com/challenges/np-shape-reshape/problem
# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
# https://www.hackerrank.com/challenges/np-concatenate/problem
# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
# https://www.hackerrank.com/challenges/np-eye-and-identity/problem
# https://www.hackerrank.com/challenges/np-array-mathematics/problem
# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
# https://www.hackerrank.com/challenges/np-sum-and-prod/problem
# https://www.hackerrank.com/challenges/np-min-and-max/problem
# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
# https://www.hackerrank.com/challenges/np-dot-and-cross/problem
# https://www.hackerrank.com/challenges/np-inner-and-outer/problem
# https://www.hackerrank.com/challenges/np-polynomials/problem
# https://www.hackerrank.com/challenges/np-linear-algebra/problem
"""
Docstring for NumpyFuntions
Author: Aquilas DJENONTIN
    This module demonstrates the use of various numpy functions to perform operations on arrays, such as reshaping, transposing, flattening, concatenating, creating arrays of zeros and ones, creating identity matrices, performing array mathematics, rounding elements, calculating sums and products, finding minimum and maximum values, calculating mean, variance, and standard deviation, calculating dot and cross products, calculating inner and outer products, working with polynomials, and performing linear algebra operations.
    Each function in this module is designed to demonstrate a specific numpy function or set of functions, and includes a docstring that explains the purpose of the function and its complexity.
    The example usage at the end of the module shows how to use the arrays function to convert a list of strings to a numpy array of floats and reverse it.
    Note: The input for the example usage should be a list of strings representing numbers, separated by spaces. For example: "1 2 3 4 5".
"""

import numpy as np


def arrays(arr):
    """
    Convert a list of strings to a numpy array of floats and reverse it.
    Complexity: O(n) where n is the length of the input list, since we need to iterate through the list to convert each element to a float and reverse the array.
    """
    # Convert the list of strings to a numpy array of floats
    np_array = np.array(arr, dtype=float)
    # Reverse the array
    reversed_array = np_array[::-1]
    return reversed_array


def demo_reshape(arr):
    """
    Demonstrate the use of numpy's reshape function to change the shape of an array.
    Complexity: O(1) since we are performing a constant number of operations to reshape the array.
    """
    arr = np.reshape(arr, (3, 3))  # Reshape the array to 3x3
    return arr  # Return the shape of the array


def demo_transpose(arr):
    """
    Demonstrate the use of numpy's transpose function to change the orientation of an array.
    Complexity: O(1) since we are performing a constant number of operations to transpose the array.
    """
    arr = np.transpose(arr)  # Transpose the array
    return arr  # Return the transposed array


def demo_flatten(arr):
    """
    Demonstrate the use of numpy's flatten function to convert a multi-dimensional array into a 1D array.
    Complexity: O(1) since we are performing a constant number of operations to flatten the array.
    """
    arr = np.flatten(arr)  # Flatten the array
    return arr  # Return the flattened array


def demo_concatenate(arr1, arr2):
    """
    Demonstrate the use of numpy's concatenate function to join two arrays along a specified axis.
    Complexity: O(n) where n is the total number of elements in the resulting array, since we need to iterate through all elements to concatenate them.
    """
    arr = np.concatenate(
        (arr1, arr2), axis=0
    )  # Concatenate the two arrays along the first axis
    return arr  # Return the concatenated array


def demo_zeros_and_ones(shape):
    """
    Demonstrate the use of numpy's zeros and ones functions to create arrays filled with zeros and ones.
    Complexity: O(n) where n is the total number of elements in the resulting array, since we need to iterate through all elements to fill them with zeros or ones.
    """
    zeros_array = np.zeros(shape)  # Create an array filled with zeros
    ones_array = np.ones(shape)  # Create an array filled with ones
    return zeros_array, ones_array  # Return both arrays


def demo_eye_and_identity(n):
    """
    Demonstrate the use of numpy's eye and identity functions to create identity matrices.
    Complexity: O(n^2) where n is the size of the resulting square matrix, since we need to iterate through all elements to fill them with zeros and ones.
    """
    eye_array = np.eye(n)  # Create an identity matrix using the eye function
    identity_array = np.identity(
        n
    )  # Create an identity matrix using the identity function
    return eye_array, identity_array  # Return both arrays


def demo_array_mathematics(arr1, arr2):
    """
    Demonstrate the use of numpy's array mathematics functions to perform element-wise operations on arrays.
    Complexity: O(n) where n is the total number of elements in the resulting array, since we need to iterate through all elements to perform the operations.
    """
    sum_array = np.add(arr1, arr2)  # Element-wise addition
    diff_array = np.subtract(arr1, arr2)  # Element-wise subtraction
    prod_array = np.multiply(arr1, arr2)  # Element-wise multiplication
    div_array = np.divide(arr1, arr2)  # Element-wise division
    floor_div_array = np.floor_divide(arr1, arr2)  # Element-wise floor division
    mod_array = np.mod(arr1, arr2)  # Element-wise modulus
    power_array = np.power(arr1, arr2)  # Element-wise exponentiation
    return (
        sum_array,
        diff_array,
        prod_array,
        div_array,
        floor_div_array,
        mod_array,
        power_array,
    )  # Return all results


def demo_floor_ceil_rint(arr):
    """
    Demonstrate the use of numpy's floor, ceil, and rint functions to round elements of an array.
    Complexity: O(n) where n is the total number of elements in the resulting array, since we need to iterate through all elements to perform the rounding operations.
    """
    floor_array = np.floor(arr)  # Round down to the nearest integer
    ceil_array = np.ceil(arr)  # Round up to the nearest integer
    rint_array = np.rint(arr)  # Round to the nearest integer
    return floor_array, ceil_array, rint_array  # Return all results


def demo_sum_prod(arr):
    """
    Demonstrate the use of numpy's sum and prod functions to calculate the sum and product of array elements.
    Complexity: O(n) where n is the total number of elements in the resulting array, since we need to iterate through all elements to calculate the sum and product.
    """
    sum_array = np.sum(arr)  # Calculate the sum of all elements
    prod_array = np.prod(arr)  # Calculate the product of all elements
    return sum_array, prod_array  # Return both results


def demo_min_max(arr):
    """
    Demonstrate the use of numpy's min and max functions to find the minimum and maximum values in an array.
    Complexity: O(n) where n is the total number of elements in the resulting array, since we need to iterate through all elements to find the minimum and maximum values.
    """
    min_value = np.min(arr)  # Find the minimum value in the array
    max_value = np.max(arr)  # Find the maximum value in the array
    return min_value, max_value  # Return both results


def demo_mean_var_std(arr):
    """
    Demonstrate the use of numpy's mean, var, and std functions to calculate the mean, variance, and standard deviation of array elements.
    Complexity: O(n) where n is the total number of elements in the resulting array, since we need to iterate through all elements to calculate the mean, variance, and standard deviation.
    """
    mean_value = np.mean(arr)  # Calculate the mean of the array
    var_value = np.var(arr)  # Calculate the variance of the array
    std_value = np.std(arr)  # Calculate the standard deviation of the array
    return mean_value, var_value, std_value  # Return all results


def demo_dot_cross(arr1, arr2):
    """
    Demonstrate the use of numpy's dot and cross functions to calculate the dot product and cross product of two arrays.
    Complexity: O(n) where n is the total number of elements in the resulting array, since we need to iterate through all elements to calculate the dot and cross products.
    """
    dot_product = np.dot(arr1, arr2)  # Calculate the dot product of the two arrays
    cross_product = np.cross(
        arr1, arr2
    )  # Calculate the cross product of the two arrays
    return dot_product, cross_product  # Return both results


def demo_inner_outer(arr1, arr2):
    """
    Demonstrate the use of numpy's inner and outer functions to calculate the inner product and outer product of two arrays.
    Complexity: O(n) where n is the total number of elements in the resulting array, since we need to iterate through all elements to calculate the inner and outer products.
    """
    inner_product = np.inner(
        arr1, arr2
    )  # Calculate the inner product of the two arrays
    outer_product = np.outer(
        arr1, arr2
    )  # Calculate the outer product of the two arrays
    return inner_product, outer_product  # Return both results


def demo_polynomials(coefficients, x):
    """
    Demonstrate the use of numpy's poly1d function to create a polynomial from given coefficients and evaluate it at a specific value of x.
    Complexity: O(n) where n is the degree of the polynomial, since we need to iterate through all coefficients to evaluate the polynomial at the given value of x.
    """
    polynomial = np.poly1d(
        coefficients
    )  # Create a polynomial from the given coefficients
    result = polynomial(x)  # Evaluate the polynomial at the given value of x
    return result  # Return the result


def demo_linear_algebra(arr):
    """
    Demonstrate the use of numpy's linear algebra functions to perform various operations on arrays, such as calculating the determinant, inverse, and eigenvalues.
    Complexity: O(n^3) where n is the size of the resulting square matrix, since we need to perform matrix operations that typically have cubic time complexity.
    """
    determinant = np.linalg.det(arr)  # Calculate the determinant of the array
    inverse = np.linalg.inv(arr)  # Calculate the inverse of the array
    eigenvalues, eigenvectors = np.linalg.eig(
        arr
    )  # Calculate the eigenvalues and eigenvectors of the array
    return determinant, inverse, eigenvalues, eigenvectors  # Return all results


# Example usage:
if __name__ == "__main__":
    arr = input().strip().split()
    result = arrays(arr)
    print(result)
