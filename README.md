# Strings and Control Flow practice

This project consists of small assignment functions to work in groups and practice control flow and strings methods. It'll also be useful to introduce you to our Github workflow.

## How to run tests

**Run tests for just one assignment**

```bash
$ py.test -v --tb=short group_project/assignment_1.py
```

![image](https://user-images.githubusercontent.com/872296/28190829-e38ca940-67fa-11e7-8e3a-d363ac5aecd8.png)

**Run tests matching a given name**

```bash
$ py.test -v --tb=short group_project/assignment_1.py -k odd
```

![image](https://user-images.githubusercontent.com/872296/28190860-0ec010ca-67fb-11e7-893a-8765295826b9.png)

**Run all the tests**

```bash
$ py.test -v --tb=short group_project

# OR

$ make test
```

**Testing Python versions with TOX**

```bash
$ tox -epy27
```

![image](https://user-images.githubusercontent.com/872296/28190983-c13b11f0-67fb-11e7-93d2-c93f9f601072.png)
