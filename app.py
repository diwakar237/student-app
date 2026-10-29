def calculate_results(marks_list):
    total = sum(marks_list)
    average = total / len(marks_list) if marks_list else 0
    
    # New grade logic requirement
    if average >= 90:
        grade = 'A'
    elif average >= 75:
        grade = 'B'
    elif average >= 50:
        grade = 'C'
    else:
        grade = 'F'
        
    return {"total": total, "average": round(average, 2), "grade": grade}

if __name__ == "__main__":
    print("--- Student Marks & Grade Calculator ---")
    sample_marks = [80, 85, 90]
    results = calculate_results(sample_marks)
    print(f"Marks: {sample_marks}")
    print(f"Total: {results['total']}, Average: {results['average']}, Grade: {results['grade']}")
