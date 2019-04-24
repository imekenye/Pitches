from flask import  render_template,redirect,request,url_for,abort,flash
from . import main
from .forms import UpdateProfile,SubmitPitch,CommentForm
from .. import db,photos
# from ..static import photos
from flask_login import login_required
from ..models import User,Pitch,Comments

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to Pitch'

    return render_template('index.html', title=title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    index=Pitch.query.all()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, index=index)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/pitchsubmit',methods=['GET', 'POST'])
@login_required
def submit_pitch():
    form = SubmitPitch()


    if form.validate_on_submit():
        pitch = Pitch(post=form.post.data, body=form.body.data,category=form.category.data)
        pitch.save_pitch()

        # flash('Pitch added successfully')

        return redirect(url_for('main.index'))
    return render_template('pitchsubmit.html', form=form)

# comments
@main.route('/comments', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    pitch = Pitch.query.get(id)
    if form.validate_on_submit():
        comment = Comments(title=form.title.data,comment=form.comment.data, pitch=pitch)
        db.session.add(comment)
        db.session.commit()
    com_ment = Comments.query.filter_by(pitch=pitch).all()
    return render_template('comment.html',com_ment=com_ment,form=form)
