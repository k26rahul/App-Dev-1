class TodoItem:
  last_idx = 1

  def __init__(self, text):
    self.id = TodoItem.last_idx
    TodoItem.last_idx += 1

    self.text = text
    self.status = 'pending'
