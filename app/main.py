from flask import render_template, request
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, or_
from load_db import ROW_DATA


app = Flask(__name__)
app.config['SECRET_KEY'] = 'a very very very long secret key'
engine = create_engine("postgresql+psycopg2://postgres:postgres@postgres:5432/cats_db")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@postgres:5432/cats_db'
db = SQLAlchemy(app)


class Cat(db.Model):
	__tablename__ = 'cat'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), nullable=False)
	description = db.Column(db.Text())
	breed = db.Column(db.String(255))
	age = db.Column(db.Integer)
	img = db.Column(db.String)

	def __repr__(self):
		return f'{self.name}'


with app.app_context():
	db.create_all()
	# Clear table cat
	engine.execute('TRUNCATE TABLE cat RESTART IDENTITY;')
	# insert data to the table 'cat'
	for obj in ROW_DATA:
		db.session.add(Cat(**obj))
		db.session.flush()
	db.session.commit()


@app.route('/<sort_field>')
@app.route('/')
def index(sort_field=None):
	page = request.args.get('page', 1, type=int)

	if sort_field in ('name', 'breed', 'age'):
		cats = Cat.query.order_by(sort_field).paginate(page=page, per_page=4)
	else:
		cats = Cat.query.paginate(page=page, per_page=4)

	return render_template('index.html', cats=cats, sort_field=sort_field)


@app.route('/search')
def get_search():
	page = request.args.get('page', 1, type=int)
	find = request.args.get('find', None)
	cats_find = Cat.query.filter(or_(Cat.name.ilike(f'%{find}%'),
	                                 Cat.breed.ilike(f'%{find}%'),
	                                 Cat.description.ilike(f'%{find}%'))). \
		paginate(page=page, per_page=4)
	return render_template('index.html', cats=cats_find)


@app.route('/cat/<int:pk>')
def cat_detail(pk):
	cat = Cat.query.get(pk)
	return render_template('cat_detail.html', cat=cat)


@app.route('/about')
def about():
	return render_template('about.html')


app.run(debug=True, host="0.0.0.0", port="5000")
