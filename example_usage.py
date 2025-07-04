"""
Example Usage of Linear Regression Analysis Script
Author: Jatin Gupta (Data Science Intern)

This script shows how to use the LinearRegressionAnalysis class
in different ways. Very helpful for beginners!
"""

# Import our custom linear regression class
from linear_regression_analysis import LinearRegressionAnalysis

def example_with_sample_data():
    """
    Example 1: Using built-in sample data
    This is the easiest way to get started!
    """
    print("=" * 60)
    print("EXAMPLE 1: Using Built-in Sample Data")
    print("=" * 60)
    
    # Create the analysis object
    lr = LinearRegressionAnalysis()
    
    # Load sample data (house size vs price)
    lr.load_sample_data()
    
    # Train the model
    lr.fit_model()
    
    # Show results
    lr.model_summary()
    
    # Make predictions
    new_sizes = [1200, 1800, 2500]
    lr.predict_new_values(new_sizes)
    
    print("\n✅ Example 1 completed successfully!")

def example_with_custom_data():
    """
    Example 2: Using your own custom data
    This shows how to use the tool with your own dataset!
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Using Custom Data")
    print("=" * 60)
    
    # Create the analysis object
    lr = LinearRegressionAnalysis()
    
    # Example: Student study hours vs exam scores
    study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Hours studied
    exam_scores = [45, 52, 58, 65, 72, 78, 85, 88, 92, 95]  # Exam scores
    
    print("📚 Analyzing relationship between study hours and exam scores...")
    
    # Load custom data
    lr.load_custom_data(study_hours, exam_scores)
    
    # Train the model
    lr.fit_model()
    
    # Show results
    lr.model_summary()
    
    # Make predictions for new study hours
    new_hours = [2.5, 5.5, 8.5]
    predictions = lr.predict_new_values(new_hours)
    
    print("\n✅ Example 2 completed successfully!")

def example_step_by_step():
    """
    Example 3: Step by step analysis
    This shows each step in detail for learning purposes!
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Step-by-Step Analysis")
    print("=" * 60)
    
    # Step 1: Initialize
    print("\n🔹 Step 1: Initialize the analysis tool")
    lr = LinearRegressionAnalysis()
    
    # Step 2: Prepare data
    print("\n🔹 Step 2: Prepare some sample data")
    # Simple example: Temperature vs Ice cream sales
    temperature = [20, 25, 30, 35, 40, 45, 50]  # Temperature in Celsius
    ice_cream_sales = [100, 150, 200, 280, 350, 400, 480]  # Sales in units
    
    print("📊 Data: Temperature vs Ice Cream Sales")
    for temp, sales in zip(temperature, ice_cream_sales):
        print(f"  {temp}°C → {sales} units")
    
    # Step 3: Load data
    print("\n🔹 Step 3: Load data into the model")
    lr.load_custom_data(temperature, ice_cream_sales)
    
    # Step 4: Train model
    print("\n🔹 Step 4: Train the linear regression model")
    lr.fit_model()
    
    # Step 5: Analyze results
    print("\n🔹 Step 5: Analyze the results")
    lr.model_summary()
    
    # Step 6: Make predictions
    print("\n🔹 Step 6: Make predictions for new temperatures")
    new_temps = [28, 38, 48]
    lr.predict_new_values(new_temps)
    
    print("\n✅ Example 3 completed successfully!")

def main():
    """
    Main function to run all examples
    """
    print("🎯 Welcome to Linear Regression Examples!")
    print("This script demonstrates different ways to use linear regression.")
    print("Created by: Jatin Gupta (Data Science Intern)")
    print("Let's explore various examples! 🚀\n")
    
    try:
        # Run all examples
        example_with_sample_data()
        example_with_custom_data()
        example_step_by_step()
        
        print("\n" + "=" * 60)
        print("🎉 ALL EXAMPLES COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        print("\n💡 Key Takeaways:")
        print("1. Linear regression finds the best line through your data points")
        print("2. R-squared tells you how well the line fits (higher is better)")
        print("3. You can use the trained model to make predictions")
        print("4. Always visualize your data to understand patterns")
        print("5. Clean data leads to better models")
        
        print("\n📚 Next Steps:")
        print("• Try with your own data!")
        print("• Experiment with different datasets")
        print("• Learn about multiple linear regression")
        print("• Explore other machine learning algorithms")
        
        print("\n😊 Thank you for learning with us!")
        print("Happy coding! - Jatin Gupta")
        
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        print("\nPlease make sure you have installed all required packages:")
        print("pip install numpy scikit-learn matplotlib pandas")

if __name__ == "__main__":
    main()