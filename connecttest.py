from pymodm import connect, MongoModel, fields

connect("mongodb+srv://jjb80:Jimbo4463@bme547.kediv.mongodb.net/bme547?retryWrites=true&w=majority")

class User(MongoModel):
    name=fields.CharField()
    
x = User(name="Jimmy")
x.save()
