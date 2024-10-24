def greet(name):
  return f'good morning {name}!'

# def greet_divya():
#   return 'good morning divya!'


# def greet_vidu():
#   return 'good morning vidu!'


# def greet_harikesh():
#   return 'good morning harikesh!'


def add(a, b):
  return a + b


def calc(operator, a, b):
  if operator == 'add':
    return a + b
  elif operator == 'minus':
    return a - b
  elif operator == 'mult':
    return a * b
  elif operator == 'div':
    return a / b


print(greet('gauri'))
