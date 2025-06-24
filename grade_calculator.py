def calculate_grade(assignments):
    """
    Calculates the weighted average grade from a list of assignments.

    Args:
        assignments (list of tuples): Each tuple contains:
            - name (str)
            - grade (float)
            - weight (float)

    Returns:
        Final weighted grade
        Returns 0 if no assignments are provided.
    """

    if not assignments:
        return 0

    total_weighted_score = 0 

    for assignment in assignments:
        name = assignment[0]     
        grade = assignment[1]    
        weight = assignment[2]  

        total_weighted_score += grade * (weight / 100)

    return total_weighted_score