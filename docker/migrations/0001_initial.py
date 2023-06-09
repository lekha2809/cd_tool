# Generated by Django 4.2 on 2023-04-24 03:49

from django.db import migrations, models
import django.db.models.deletion
import yamlfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeployEnvironment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('app_env', models.CharField(max_length=255)),
                ('swarm_manager', models.CharField(max_length=255)),
                ('more_info', yamlfield.fields.YAMLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DockerComposeTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default', max_length=255, unique=True)),
                ('docker_compose_template', yamlfield.fields.YAMLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NginxTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('template', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bitbucket_slug', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('cd_name', models.CharField(max_length=255, null=True)),
                ('type', models.CharField(default='api', max_length=255)),
                ('image_name', models.CharField(max_length=255, null=True)),
                ('nginx_port', models.IntegerField(blank=True, default=80, null=True)),
                ('service_port', models.IntegerField(blank=True, default=8080, null=True)),
                ('scheduler_rule', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.BooleanField(blank=True, default=False)),
                ('deploy_template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='docker.dockercomposetemplate')),
                ('nginx_template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='docker.nginxtemplate')),
            ],
        ),
        migrations.CreateModel(
            name='DeployHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=255)),
                ('commit_tag', models.CharField(max_length=255, null=True)),
                ('docker_compose', yamlfield.fields.YAMLField(null=True)),
                ('scheduler_info', yamlfield.fields.YAMLField(null=True)),
                ('scale', models.IntegerField(null=True)),
                ('env', models.CharField(max_length=255, null=True)),
                ('deploy_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='success', max_length=255)),
                ('desc', models.TextField(max_length=255, null=True)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='docker.service')),
            ],
        ),
        migrations.CreateModel(
            name='ActiveServiceOnEnv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=False)),
                ('env', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docker.deployenvironment')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docker.service')),
            ],
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('container_name', models.CharField(max_length=255, null=True)),
                ('public_port', models.IntegerField(blank=True, default=0, null=True)),
                ('docker_node', models.CharField(blank=True, max_length=255, null=True)),
                ('scheduler_rule', models.CharField(blank=True, max_length=255, null=True)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('more_info', models.TextField(blank=True, max_length=255, null=True)),
                ('image_tag', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, default='unknown', max_length=100, null=True)),
                ('env', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='docker.deployenvironment')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='docker.service')),
            ],
            options={
                'unique_together': {('container_name', 'env'), ('docker_node', 'public_port', 'env')},
            },
        ),
    ]
