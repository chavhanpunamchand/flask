from flask_initial_web_service_new.model import *
from flask import Flask,request,render_template,session


@app.route('/accounts/',methods=['GET','POST'])
def save_or_update_accounts():
    if 'userinfo' in session:
        msg  = ''
        if request.method == 'POST':
            accno = int(request.form['accno'])
            acctype = request.form['accty']
            accbal = request.form['accbal']
            dbacc = Account.query.filter_by(id=accno).first()
            if dbacc:
                dbacc.type = acctype
                dbacc.balance = accbal
                db.session.commit()
                msg = "Acccount Updated Successfully..!"
            else:
                dbacc = Account(id=accno,type=acctype,balance=accbal)
                db.session.add(dbacc)
                db.session.commit()
                msg = "Account Created Successfully...!"

        return render_template('accounts.html',
                               resp = msg,user=session['userinfo'],
                               account = Account.dummy_account(),
                               acclist = Account.query.all())
    return render_template('login.html', resp='')
@app.route('/accounts/edit/<int:acid>')
def edit_account_info(acid):
    if 'userinfo' in session:
        return render_template('accounts.html',
                               resp='',user=session['userinfo'],
                               account=Account.query.filter_by(id=acid).first(),
                               acclist=Account.query.all())
    return render_template('login.html', resp='')
@app.route('/accounts/delete/<int:acid>')
def delete_account_info(acid):
    if 'userinfo' in session:
        msg = ''
        acc = Account.query.filter_by(id=acid).first()
        if acc:
            db.session.delete(acc)
            db.session.commit()
            msg = "Account Removed Successfully..!"
        return render_template('accounts.html',
                               resp=msg,user=session['userinfo'],
                               account=Account.dummy_account(),
                               acclist=Account.query.all())
    return render_template('login.html', resp='')

if __name__ == '__main__':
    app.run(debug=True)