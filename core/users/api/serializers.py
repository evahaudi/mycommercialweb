from rest_framework import serializers
from users.models import Users, Freelancer, Client

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields = ['id', 'username', 'email', 'is_freecancer', 'is_client']

class FreelanceSignupView(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model=Users
        fields = ['id','username','email','phone', 'company_name','skills', 'description', 'portfolio','password2','password']
        extra_kwargs={
            'password':{'write_only':True}
        }
        
    def save(self, **kwargs):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        skills = self.validated_data['skills']
        description = self.validated_data['description']
        portfolio = self.validated_data['portfolio'],
        phone = self.validated_data['phone'],
        company_name=self.validated_data['company_name']

        if password != password2:
            raise serializers.ValidationError({"error": "Passwords do not match"})

        user = Users(
            username=username,
            email=email,
            skills=skills,
            description=description,
            portfolio=portfolio,
            phone=phone,
            company_name=company_name
        )
        user.set_password(password)
        user.is_freecancer = True
        user.save()
        Freelancer.objects.create(user=user)
        return user
        
class ClientSignupView(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model=Users
        fields = ['id','username','email','phone', 'company_name','skills', 'description', 'portfolio','password2','password']
        extra_kwargs={
            'password':{'write_only':True}
        }
        
    def save(self, **kwargs):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        skills = self.validated_data['skills']
        description = self.validated_data['description']
        portfolio = self.validated_data['portfolio']
        phone = self.validated_data['phone']
        company_name=self.validated_data['company_name']
        if password != password2:
            raise serializers.ValidationError({"error": "Passwords do not match"})

        user = Users(
            username=username,
            email=email,
            skills=skills,
            description=description,
            portfolio=portfolio,
            phone=phone,
            company_name=company_name
        )
        user.set_password(password)
        user.is_client = True
        user.save()
        Client.objects.create(user=user)
        return user
