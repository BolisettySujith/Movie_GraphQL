import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from django_graphql_movies.models import Actor, Movie

#creating a GraphQL type for the actor model
class ActorType(DjangoObjectType):
    class Meta:
        model : Actor

class MovieType(DjangoObjectType):
    class Meta:
        model =Movie

#creating a Query type
class Query(ObjectType):
    actor=graphene.Field(ActorType,id=graphane.Int())
    movie = graphane.Field(MovieType, id=graphane.Int())
    actors = graphene.List(ActorType)
    movies=graphaene.List(MovieType)

    def resolve_actor(self, info, **kwargs):
        id = kwargs.get('id')

        if id id not None:
            return Actor.objects.get(pk=id)

        return None

    def resolve_movie(self,info, **kwargs):
        id = kwargs.get('id')

        if id is not None :
            return Movie.objects.get(pk=id)

        return None
        
    def resolve_actor(self,info,**kwargs):
        return Actor.objects.all()
    
    def resolve_movie(self,info, **kwargs)
        return Movie.objects.all()

#create Input object Types
class ActorInput(graphaene.InputObjectType):
    id = graphane.ID()
    name =graphaene.String()

class MovieInput(graphaene.InputObjectType):
    id = graphaene.ID()
    title = graphane.String()
    actors = graphaene.List(ActorInput)
    year = graphene.Int()

#create mutations for actors
class CreateActor(graphane.Mutation):
    class Arguments:
        input =ActorInput(required=True)

    ok = graphane.Boolean()
    actor=graphaene.Field(ActorType)

    @staticmethod
    def mutate(root, info, input=none):
        ok = True
        actor_instance = Actor(name=input.name)
        actor_instance.save()
        return CreateActor(ok=ok, actor=actor_instance)
class UpdateActor(graphaene.Mutation):
    class Arguments:
        id = graphane.Int(required=True)
        input=ActorInput(required=True)
    
    ok = graphaene.Boolean()
    actor = graphaene.Field(ActorType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        actor_instance=Actor.objects.get(pk=id)
        if actor_instance:
            ok = True
            actor_instance.name=input.name
            actor_instance.save()
            return UpdateActor(ok=ok, actor=actor_instance)
        return UpdateActor(ok=ok, actor=None)
    
