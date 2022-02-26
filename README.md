# `app` endpoints
## `keys_missing`
```Returns true if any keys are missing from data.```

## `new_exam`
```
    Creates a new exam from a list of supplied questions.
    
    Example JSON body:
        {
            "teacherID": "teacherID_001",  /* via Cookie */
            "assignees": [
                "studentID_001",
                "studentID_002",
                ...
            ],
            "questions": [{
                "questionID": "questionID_001",
                "points": 10
            },
            {
                "questionID": "questionID_002",
                "points": 6
            }]
        } 

    Returns:
        ({
            "examID": "examID_008" /* after db insert */
        }, 201)
    ```

## `show_questions`
```None```

## `submit_exam`
```
    Accepts a student's exam submission.
    
    Expected JSON body:
        {
            “examID”: “examID_001”,
            “studentID”: “studentID_001”,
            “submission”: [{
                “questionID”: “questionID_001”,
                “response”: “def foo(x):
    return x”
            },
            {
                “questionID”: “questionID_002”,
                “response”: “def foo(x):
    return x”
            }]
        }

    Returns:
        ({
            "submissionID": "submissionID_001" /* after db insert */
        }, 201)
    ```

# `exams` endpoints
## `keys_missing`
```Returns true if any keys are missing from data.```

## `new_exam`
```
    Creates a new exam from a list of supplied questions.
    
    Example JSON body:
        {
            "teacherID": "teacherID_001",  /* via Cookie */
            "assignees": [
                "studentID_001",
                "studentID_002",
                ...
            ],
            "questions": [{
                "questionID": "questionID_001",
                "points": 10
            },
            {
                "questionID": "questionID_002",
                "points": 6
            }]
        } 

    Returns:
        ({
            "examID": "examID_008" /* after db insert */
        }, 201)
    ```

## `show_questions`
```None```

## `submit_exam`
```
    Accepts a student's exam submission.
    
    Expected JSON body:
        {
            “examID”: “examID_001”,
            “studentID”: “studentID_001”,
            “submission”: [{
                “questionID”: “questionID_001”,
                “response”: “def foo(x):
    return x”
            },
            {
                “questionID”: “questionID_002”,
                “response”: “def foo(x):
    return x”
            }]
        }

    Returns:
        ({
            "submissionID": "submissionID_001" /* after db insert */
        }, 201)
    ```

# `login` endpoints
## `keys_missing`
```Returns true if any keys are missing from data.```

## `new_exam`
```
    Creates a new exam from a list of supplied questions.
    
    Example JSON body:
        {
            "teacherID": "teacherID_001",  /* via Cookie */
            "assignees": [
                "studentID_001",
                "studentID_002",
                ...
            ],
            "questions": [{
                "questionID": "questionID_001",
                "points": 10
            },
            {
                "questionID": "questionID_002",
                "points": 6
            }]
        } 

    Returns:
        ({
            "examID": "examID_008" /* after db insert */
        }, 201)
    ```

## `show_questions`
```None```

## `submit_exam`
```
    Accepts a student's exam submission.
    
    Expected JSON body:
        {
            “examID”: “examID_001”,
            “studentID”: “studentID_001”,
            “submission”: [{
                “questionID”: “questionID_001”,
                “response”: “def foo(x):
    return x”
            },
            {
                “questionID”: “questionID_002”,
                “response”: “def foo(x):
    return x”
            }]
        }

    Returns:
        ({
            "submissionID": "submissionID_001" /* after db insert */
        }, 201)
    ```

# `questions` endpoints
## `keys_missing`
```Returns true if any keys are missing from data.```

## `new_exam`
```
    Creates a new exam from a list of supplied questions.
    
    Example JSON body:
        {
            "teacherID": "teacherID_001",  /* via Cookie */
            "assignees": [
                "studentID_001",
                "studentID_002",
                ...
            ],
            "questions": [{
                "questionID": "questionID_001",
                "points": 10
            },
            {
                "questionID": "questionID_002",
                "points": 6
            }]
        } 

    Returns:
        ({
            "examID": "examID_008" /* after db insert */
        }, 201)
    ```

## `show_questions`
```None```

## `submit_exam`
```
    Accepts a student's exam submission.
    
    Expected JSON body:
        {
            “examID”: “examID_001”,
            “studentID”: “studentID_001”,
            “submission”: [{
                “questionID”: “questionID_001”,
                “response”: “def foo(x):
    return x”
            },
            {
                “questionID”: “questionID_002”,
                “response”: “def foo(x):
    return x”
            }]
        }

    Returns:
        ({
            "submissionID": "submissionID_001" /* after db insert */
        }, 201)
    ```

