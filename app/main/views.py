from flask import  render_template,redirect,request,url_for,abort,flash
from . import main
from .forms import UpdateProfile,SubmitPitch
from .. import db,photos
# from ..static import photos
from flask_login import login_required
from ..models import User,Pitch

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

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

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

@main.route('/user/<user_id>',methods=['GET', 'POST'])
@login_required
def submit_pitch(user_id):
    form = SubmitPitch()
    form.user_id.data = user_id

    if form.validate_on_submit():
        pitch = Pitch(post=form.post.data, body=form.body.data,category=form.category.data)

        db.session.add(pitch)
        db.session.commit()
        flash('Pitch added successfully')

        return redirect(url_for('pitches.html',user_id=pitch.user_id))
    return render_template('pitchsubmit.html', form=form, user_id=user_id)
