from asyncio import Future

my_f = Future()

print(f'is my future done? {my_f.done()}')

my_f.set_result(42)
print(f'is my future done? {my_f.done()}')
print(f'my_future result is {my_f.result()}')
