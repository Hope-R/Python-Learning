# Global
name = "I am global"

def greet():
    # Enclosing
    name = "Enclosing"

    def hello():
        # Local
        name = "I am a local"
        print(name)

    hello()

greet()
# print(a)
