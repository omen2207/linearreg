import csv

def read_data(csv_file):
    x_values = []
    y_values = []
    with open(csv_file, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            x_values.append(float(row[0]))
            y_values.append(float(row[1]))
    return x_values, y_values

def calculate_coefficients(x_values, y_values):
    n = len(y_values)
    x_mean = sum(x_values) / n
    y_mean = sum(y_values) / n

    a= sum((x_values[i] - x_mean) * (y_values[i] - y_mean) for i in range(n))
    b = sum((x_values[i] - x_mean) ** 2 for i in range(n))
    
    m = a / b
    b = y_mean - m * x_mean
    return b, m

def main():
    csv_file = r'C:\Users\bhilw\OneDrive\Documents\DM\14_linear_regression\data.csv'
    x_values, y_values = read_data(csv_file)
    b0, b1 = calculate_coefficients(x_values, y_values)
    print(f"Slope (m): {b1:.4f}")
    print(f"Intercept (c): {b0:.4f}")
    print(f"Linear Equation: y = {b1:.4f} * x + {b0:.4f}")

if __name__ == "__main__":
    main()
