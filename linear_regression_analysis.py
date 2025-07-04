"""
Linear Regression Analysis Script
Author: Jatin Gupta (Data Science Intern)
Date: July 2025

This script demonstrates simple linear regression analysis using Python.
Kindly ensure you have the required libraries installed before running.

Dependencies required:
- numpy
- scikit-learn  
- matplotlib
- pandas

To install: pip install numpy scikit-learn matplotlib pandas
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

class LinearRegressionAnalysis:
    """
    A comprehensive class for performing linear regression analysis.
    
    This class is designed to make linear regression analysis very simple and 
    straightforward for anyone to understand and use, even beginners.
    """
    
    def __init__(self):
        """
        Initialize the LinearRegressionAnalysis class.
        Setting up the model and other variables properly.
        """
        self.model = LinearRegression()
        self.X = None
        self.y = None
        self.y_pred = None
        self.is_fitted = False
        
        print("🚀 Linear Regression Analysis tool initialized successfully!")
        print("Created by: Jatin Gupta (Data Science Intern)")
        print("Ready to perform some amazing analysis! 📊")
    
    def load_sample_data(self):
        """
        Generate sample data for demonstration purposes.
        
        This method creates synthetic data that shows a linear relationship
        between house size and house price (a classic example, isn't it?).
        """
        print("\n📈 Generating sample data...")
        print("Creating a dataset showing relationship between house size and price")
        
        # Generate synthetic data - house size vs price
        np.random.seed(42)  # For reproducible results
        house_sizes = np.random.uniform(500, 3000, 100)  # House sizes in sq ft
        
        # Price calculation with some noise (to make it realistic)
        # Base price formula: 100 rupees per sq ft + some random variation
        house_prices = house_sizes * 100 + np.random.normal(0, 10000, 100)
        
        self.X = house_sizes.reshape(-1, 1)  # Reshape for sklearn
        self.y = house_prices
        
        # Create a nice DataFrame for display
        self.df = pd.DataFrame({
            'House_Size_SqFt': house_sizes,
            'House_Price_Lakhs': house_prices / 100000  # Convert to lakhs
        })
        
        print(f"✅ Sample data generated successfully!")
        print(f"Dataset contains {len(self.df)} house records")
        print("\nFirst 5 records:")
        print(self.df.head())
        
        return self.df
    
    def load_custom_data(self, X_data, y_data):
        """
        Load custom data for analysis.
        
        Parameters:
        X_data: Independent variable (features)
        y_data: Dependent variable (target)
        """
        print("\n📊 Loading custom data...")
        
        if len(X_data) != len(y_data):
            raise ValueError("Length of X_data and y_data must be same!")
        
        self.X = np.array(X_data).reshape(-1, 1)
        self.y = np.array(y_data)
        
        print(f"✅ Custom data loaded successfully!")
        print(f"Dataset size: {len(self.X)} records")
    
    def fit_model(self):
        """
        Train the linear regression model on the loaded data.
        
        This method fits the linear regression line to our data points.
        """
        if self.X is None or self.y is None:
            raise ValueError("Please load data first using load_sample_data() or load_custom_data()")
        
        print("\n🔧 Training the linear regression model...")
        
        # Fit the model
        self.model.fit(self.X, self.y)
        
        # Make predictions
        self.y_pred = self.model.predict(self.X)
        
        # Calculate performance metrics
        self.mse = mean_squared_error(self.y, self.y_pred)
        self.r2 = r2_score(self.y, self.y_pred)
        
        self.is_fitted = True
        
        print("✅ Model training completed successfully!")
        print(f"Model Coefficient (slope): {self.model.coef_[0]:.2f}")
        print(f"Model Intercept: {self.model.intercept_:.2f}")
        print(f"R-squared Score: {self.r2:.4f}")
        print(f"Mean Squared Error: {self.mse:.2f}")
        
        # Interpret the results in simple terms
        print("\n📝 Model Interpretation:")
        if hasattr(self, 'df'):
            print(f"For every 1 sq ft increase in house size, price increases by ₹{self.model.coef_[0]:.2f}")
        else:
            print(f"For every 1 unit increase in X, Y increases by {self.model.coef_[0]:.2f}")
    
    def visualize_results(self):
        """
        Create a beautiful visualization of the linear regression results.
        
        This method plots the original data points and the fitted regression line.
        """
        if not self.is_fitted:
            raise ValueError("Please fit the model first using fit_model()")
        
        print("\n📊 Creating visualization...")
        
        # Create the plot
        plt.figure(figsize=(10, 6))
        
        # Plot original data points
        plt.scatter(self.X, self.y, alpha=0.6, color='blue', label='Actual Data Points')
        
        # Plot regression line
        plt.plot(self.X, self.y_pred, color='red', linewidth=2, label='Regression Line')
        
        # Customize the plot
        plt.xlabel('House Size (sq ft)' if hasattr(self, 'df') else 'X Variable')
        plt.ylabel('House Price (₹)' if hasattr(self, 'df') else 'Y Variable')
        plt.title('Linear Regression Analysis\nBy Jatin Gupta (Data Science Intern)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Add R-squared as text on plot
        plt.text(0.05, 0.95, f'R² = {self.r2:.4f}', transform=plt.gca().transAxes, 
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        plt.tight_layout()
        plt.show()
        
        print("✅ Visualization created successfully!")
    
    def predict_new_values(self, new_X):
        """
        Make predictions on new data using the trained model.
        
        Parameters:
        new_X: New X values for prediction
        
        Returns:
        predictions: Predicted Y values
        """
        if not self.is_fitted:
            raise ValueError("Please fit the model first using fit_model()")
        
        new_X = np.array(new_X).reshape(-1, 1)
        predictions = self.model.predict(new_X)
        
        print(f"\n🔮 Predictions for new data:")
        for i, (x_val, pred) in enumerate(zip(new_X.flatten(), predictions)):
            if hasattr(self, 'df'):
                print(f"House {i+1}: {x_val:.0f} sq ft → ₹{pred:.2f} ({pred/100000:.2f} lakhs)")
            else:
                print(f"Prediction {i+1}: X={x_val:.2f} → Y={pred:.2f}")
        
        return predictions
    
    def model_summary(self):
        """
        Display a comprehensive summary of the model performance.
        """
        if not self.is_fitted:
            raise ValueError("Please fit the model first using fit_model()")
        
        print("\n" + "="*60)
        print("📋 LINEAR REGRESSION MODEL SUMMARY")
        print("="*60)
        print(f"Model Type: Simple Linear Regression")
        print(f"Dataset Size: {len(self.X)} records")
        print(f"")
        print(f"Model Equation: Y = {self.model.coef_[0]:.2f} * X + {self.model.intercept_:.2f}")
        print(f"")
        print(f"Performance Metrics:")
        print(f"  • R-squared Score: {self.r2:.4f} ({self.r2*100:.2f}%)")
        print(f"  • Mean Squared Error: {self.mse:.2f}")
        print(f"")
        
        # Interpret R-squared
        if self.r2 > 0.8:
            print("👍 Excellent model fit! The model explains the data very well.")
        elif self.r2 > 0.6:
            print("👌 Good model fit! The model captures the trend reasonably well.")
        elif self.r2 > 0.4:
            print("⚠️  Moderate model fit. Consider adding more features or checking data quality.")
        else:
            print("❌ Poor model fit. The linear model may not be suitable for this data.")
        
        print("="*60)
        print("Analysis completed by: Jatin Gupta (Data Science Intern)")
        print("="*60)


def main():
    """
    Main function to demonstrate the linear regression analysis.
    This is like a complete tutorial for anyone who wants to learn!
    """
    print("🎯 Welcome to Linear Regression Analysis Tool!")
    print("This tool will help you understand linear regression step by step.")
    print("Let's start our data science journey together! 🚀")
    
    # Initialize the analysis
    lr_analysis = LinearRegressionAnalysis()
    
    # Load sample data
    sample_data = lr_analysis.load_sample_data()
    
    # Fit the model
    lr_analysis.fit_model()
    
    # Show model summary
    lr_analysis.model_summary()
    
    # Create visualization
    lr_analysis.visualize_results()
    
    # Make some predictions
    print("\n🔮 Let's make some predictions for different house sizes:")
    new_house_sizes = [1000, 1500, 2000, 2500]
    predictions = lr_analysis.predict_new_values(new_house_sizes)
    
    print("\n💡 Tips for better linear regression:")
    print("1. Always check if your data has a linear relationship")
    print("2. Remove outliers that might affect the model")
    print("3. Ensure your data is clean and properly formatted")
    print("4. Consider adding more features for better accuracy")
    print("5. Validate your model on unseen data")
    
    print("\n🎉 Analysis completed successfully!")
    print("Thank you for using this tool. Happy learning! 😊")


if __name__ == "__main__":
    """
    Entry point of the script.
    Run this script directly to see the complete linear regression analysis in action!
    """
    print("Starting Linear Regression Analysis...")
    print("Script developed by: Jatin Gupta (Data Science Intern)")
    print("Institution: Indian Institute of Technology")
    print("Email: jatin.gupta@iit.ac.in")
    print("-" * 50)
    
    try:
        main()
    except ImportError as e:
        print("❌ Error: Missing required libraries!")
        print("Please install the required packages using:")
        print("pip install numpy scikit-learn matplotlib pandas")
        print(f"Specific error: {e}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        print("Please check your data and try again.")