"""Init

Revision ID: 8263ba18f349
Revises: 
Create Date: 2023-04-09 00:25:07.568263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8263ba18f349'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activity',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('callback', sa.String(), nullable=True),
    sa.Column('translations', sa.JSON(), server_default='{}', nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('callback'),
    sa.UniqueConstraint('weight')
    )
    op.create_table('bot_user',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('balance', sa.Numeric(precision=18, scale=2), nullable=False),
    sa.Column('is_blocked', sa.Boolean(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('login', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mood',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('callback', sa.String(), nullable=True),
    sa.Column('translations', sa.JSON(), server_default='{}', nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('callback')
    )
    op.create_table('spectrum',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('mood_id', sa.BigInteger(), nullable=False),
    sa.Column('callback', sa.String(), nullable=True),
    sa.Column('translations', sa.JSON(), server_default='{}', nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['mood_id'], ['mood.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('callback')
    )
    op.create_table('user_feedback',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('feedback', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['bot_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_state',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.Column('user_state', sa.String(), nullable=False),
    sa.Column('user_state_data', sa.JSON(), server_default='{}', nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['bot_user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('user_mood',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.Column('spectrum_id', sa.BigInteger(), nullable=True),
    sa.Column('activity_id', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['activity_id'], ['activity.id'], ),
    sa.ForeignKeyConstraint(['spectrum_id'], ['spectrum.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['bot_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.execute("""
    INSERT INTO 
        activity(callback, weight) 
    VALUES 
        ('HEALTH_CALLBACK', 1), 
        ('CHORES_CALLBACK', 2), 
        ('WORK_CALLBACK', 3), 
        ('STUDY_CALLBACK', 4), 
        ('MYSELF_CALLBACK', 5), 
        ('ENVIRONMENT_CALLBACK', 6), 
        ('SOCIAL_CALLBACK', 7), 
        ('FAMILY_CALLBACK', 8), 
        ('RELATIONSHIP_CALLBACK', 9)
    ;""")
    op.execute("""
    INSERT INTO 
        mood(callback, weight) 
    VALUES 
        ('MOOD_CALLBACK', 1),  
        ('DISPOSITION_CALLBACK', 2), 
        ('PRODUCTIVITY_CALLBACK', 3), 
        ('CONFIDENCE_CALLBACK', 4)
    ;""")
    op.execute("""
    INSERT INTO 
        spectrum(mood_id, callback, weight) 
    VALUES 
        (1, 'HAPPY_CALLBACK', 2), 
        (1, 'CONTENT_CALLBACK', 1), 
        (1, 'NEUTRAL_CALLBACK', 0), 
        (1, 'DISAPPOINTED_CALLBACK', -1), 
        (1, 'DEPRESSED_CALLBACK', -2), 
        (2, 'CALM_CALLBACK', 2), 
        (2, 'FRUSTRATED_CALLBACK', 1), 
        (2, 'IRRITATED_CALLBACK', 0), 
        (2, 'ANNOYED_CALLBACK', -1), 
        (2, 'ANGRY_CALLBACK', -2), 
        (3, 'PRODUCTIVE_CALLBACK', 2), 
        (3, 'MOTIVATED_CALLBACK', 1), 
        (3, 'INDECISIVE_CALLBACK', 0), 
        (3, 'OVERWHELMED_CALLBACK', -1), 
        (3, 'PROCRASTINATING_CALLBACK', -2), 
        (4, 'CONFIDENT_CALLBACK', 2), 
        (4, 'APPREHENSIVE_CALLBACK', 1), 
        (4, 'NERVOUS_CALLBACK', 0), 
        (4, 'STRESSED_CALLBACK', -1), 
        (4, 'ANXIOUS_CALLBACK', -2)
    ;""")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_mood')
    op.drop_table('user_state')
    op.drop_table('user_feedback')
    op.drop_table('spectrum')
    op.drop_table('mood')
    op.drop_table('bot_user')
    op.drop_table('activity')
    # ### end Alembic commands ###
