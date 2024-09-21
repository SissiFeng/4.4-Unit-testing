# Unit Testing Assignment: Color Mixer

## 📚 Introduction

This assignment focuses on unit testing using pytest. You'll implement a ColorMixer class and write unit tests to ensure its functionality. This exercise will help you understand the importance of unit testing, how to write and run tests, interpret test results, and practice test-driven development.

## 🎯 Objectives

By the end of this assignment, you should be able to:

1. Explain the purpose of unit tests
2. Write unit tests using pytest
3. Run and interpret unit test results
4. Debug code based on test results
5. Understand and apply test-driven development principles

## 🛠️ Setup

1. Ensure you have Python installed in your environment.
2. Install pytest by running `pip install pytest` in your terminal.
3. Open the `color_mixer.py` file in your preferred IDE or text editor.

## 📝 Instructions

### Step 1: Implement the ColorMixer class

Open `color_mixer.py` and implement the following methods in the ColorMixer class:

1. `mix_colors(color1, color2)`: Mix two colors and return the result.
2. `lighten_color(color, amount)`: Lighten a color by a certain amount.
3. `darken_color(color, amount)`: Darken a color by a certain amount.

### Step 2: Review the unit tests

Before implementing the ColorMixer class, take a moment to review the tests in `test_color_mixer.py`. This will give you a clear understanding of what each method should do and what edge cases to consider. Don't modify the tests, but use them as a guide for your implementation.

### Step 3: Implement the ColorMixer class

Now, open `color_mixer.py` and implement the following methods in the ColorMixer class:

1. `mix_colors(color1, color2)`: Mix two colors and return the result.
2. `lighten_color(color, amount)`: Lighten a color by a certain amount.
3. `darken_color(color, amount)`: Darken a color by a certain amount.

Use the tests as a guide for your implementation, ensuring that your methods will pass all the provided tests.

### Step 4: Debug and improve your implementation

1. If any tests fail, read the error messages carefully.
2. Go back to `color_mixer.py`, revise your code, and try again.
3. Repeat steps 3 and 4 until all tests pass.

### Step 5: Practice Test-Driven Development

1. Think of a new feature or edge case for the ColorMixer class.
2. Write a new test in `test_color_mixer.py` for this feature or case.
3. Run the tests and see the new test fail.
4. Implement the feature or handle the edge case in `color_mixer.py`.
5. Run the tests again and ensure all tests, including the new one, pass.

## 🧪 Testing

The `test_color_mixer.py` file contains tests for each method in the ColorMixer class. These tests check both the correctness of your implementation and handle invalid inputs.

## 📈 Completion Criteria

You've completed the assignment when:

1. All methods in the ColorMixer class are correctly implemented.
2. All tests in `test_color_mixer.py` pass when you run `pytest test_color_mixer.py`.
3. You've added at least one new test and corresponding functionality using the Test-Driven Development approach.

## 💡 Tips

- Start by implementing the simplest functionality that could work.
- Use the test results to guide your implementation.
- Remember to handle edge cases and invalid inputs.
- Don't hesitate to add more tests if you think of additional scenarios to cover.

## 🆘 Getting Help

If you encounter any issues or have questions:

1. Review this README file and the comments in `color_mixer.py` carefully.
2. Check the pytest documentation for guidance on writing and running tests.
3. If you're still stuck, reach out to your instructor or teaching assistant for help.

Good luck, and happy testing! 🧪🔬
