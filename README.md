# dt_matrix
 A web app that uses Decision Tree algorithm for clustering difficult subjects and classifying Grade 12 on their possible course program on their college

### Installation of required libraries
 1. `pip install Flask`
 2. `pip install Flask-SQLAlchemy`
 3. `pip install mysqlclient`
 4. `pip install flask-marshmallow`
 5. `pip install marshmallow-sqlalchemy`
 6. `conda install numpy`
 7. `conda install pandas`
 8. `conda install -c conda-forge scikit-learn`

### Create database and tables
 1. `python`
 2. `from app import db`
 3. `db.create_all()`

## Understanding the Repository
### Branches
- `prod` - The default branch, were everthing is ready to deploy.
- `main` - This branch is for testing and staging website.
- `dev` - This branch will have the latest changes.
### Commits
To spice up my commits I added emojis at the start of my message to easily determine what type of commit I done.
- ☕️ (coffee) for initial / not important changes
- 💯 (100) functions / routes / migration / etc...
- 🐛 (bug) error fixes
- ⚙️ (gear) todo stuffs
- 📓 (notebook) ReadMe / comments / instructions / documentation
