# Generated by Django 4.0.6 on 2022-07-25 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_coder', '0003_entregable_profesor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curso',
            options={'ordering': ('nombre',), 'verbose_name': 'My Course', 'verbose_name_plural': 'Mis Cursos'},
        ),
        migrations.AddField(
            model_name='entregable',
            name='estudiante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_coder.estudiantes'),
        ),
        migrations.AlterUniqueTogether(
            name='curso',
            unique_together={('nombre', 'camada')},
        ),
    ]
