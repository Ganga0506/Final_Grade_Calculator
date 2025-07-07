# Custom error class
class InvalidWeightError(Exception):
    """Raised when a grade or weight is invalid"""
    pass

def calculate_grade(assignments):
    """
    Calculates the weighted average grade from a list of assignments.

    Args:
        assignments (list of tuples): Each tuple contains:
            - name (str)
            - grade (float)
            - weight (float)

    Returns:
        Final weighted grade (Also scales down/up the grade if total weights do not equal 100).
        Returns 0 if no assignments are provided.

    Raises:
        InvalidWeightError: If any grade or weight is negative.

    """

    if not assignments:
        return 0

    total_weight = 0
    total_weighted_grade = 0 

    for assignment in assignments:
        name = assignment[0]     
        grade = assignment[1]    
        weight = assignment[2]  

        if grade < 0 or weight < 0:
            raise InvalidWeightError(f"Invalid grade or weight for {name}: grade={grade}, weight={weight}.") 

        total_weight += weight
        total_weighted_grade += grade * (weight / 100)

    if total_weight > 0 and total_weight != 100:
        total_weighted_grade = total_weighted_grade / (total_weight / 100)

    return total_weighted_grade