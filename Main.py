from flask  import *
from flask_sqlalchemy import SQLAlchemy
app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)
class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tarefa = db.Column(db.String(30), nullable = False)
    completado = db.Column(db.Boolean, default = False)

with app.app_context():
    db.create_all()

@app.route('/tasks/',methods = ['GET'])
def get_tarefas():
        tarefas = Task.query.all()
        return jsonify([{'id': t.id, 'tarefa': t.tarefa, 'completado': t.completado} for t in tarefas]) 


@app.route('/tasks/', methods = ['POST'])
def add_tarefas():
     data = request.json 
     nova_tarefa = Task(tarefa=data['tarefa']) 
     db.session.add(nova_tarefa)
     db.session.commit()
     return jsonify({'message': 'Tarefa adicionada com sucesso'})

@app.route('/tasks/<int:id>', methods=['PUT']) 
def update_tarefas(id):
    tarefa = Task.query.all()
    if not tarefa: 
        return jsonify({'message' : 'Tarefa não encontrada'}), 404
    tarefa_atualizada = request.json.get('Tarefa completada ', tarefa_atualizada)
    db.session.commit()
    return jsonify({'message': 'tarefa atualizada'})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_tarefa(id):
    tarefa = Task.query.all()
    if not tarefa: 
        return jsonify({'message' : 'Tarefa não encontrada'}), 404
    db.session.delete(tarefa)
    db.session.commit()
    return jsonify({'message' : 'tarefa excluida '})
if __name__:
    app.run(debug=True)


