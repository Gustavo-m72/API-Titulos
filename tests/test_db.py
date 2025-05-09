from sqlalchemy import select

from models import Apelido, User


def test_create_user(session):
    new_user = User(discordid='1329487132569636975')
    session.add(new_user)
    session.commit()

    user = session.scalar(
        select(User).where(User.discordid == '1329487132569636975')
    )

    assert user.discordid == '1329487132569636975'


def test_create_apelido_with_user(session):
    new_apelido = Apelido(
        apelido='Test Apelido',
        user_id='1329487132569636975',
        disponibilidade='disponivel',
    )
    session.add(new_apelido)
    session.commit()
    apelido = session.scalar(
        select(Apelido).where(Apelido.apelido == 'Test Apelido')
    )
    assert apelido.apelido == 'Test Apelido'
    assert apelido.user_id == '1329487132569636975'
    assert apelido.disponibilidade == 'disponivel'
    assert apelido.id == 1


def test_create_apelido_without_user(session):
    new_apelido = Apelido(
        apelido='Test Apelido',
        user_id=None,
        disponibilidade='disponivel',
    )
    session.add(new_apelido)
    session.commit()
    apelido = session.scalar(
        select(Apelido).where(Apelido.apelido == 'Test Apelido')
    )
    assert apelido.apelido == 'Test Apelido'
    assert apelido.user_id is None
    assert apelido.disponibilidade == 'disponivel'
    assert apelido.id == 1
