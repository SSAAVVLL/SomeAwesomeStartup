# Here must be our startup name

## Our white paper
> Are you tired of wasting your time picking up movies?

We want to simplify the process of selecting a film and make it personalized and relevant to your mood and interests.


### Our targets
- Parsing the film base
- Determine the mood of a movie by comment
- Determine the correlation between user interests and film genres

### Project's entitys
- Entity wich keeps and condact information about user and his interests, mood.
  - class Regular_User(BasicModel):
  - "id": int,
  - "email": str,
  - "username": str,
  - "password": str
        
- Entity which keeps films a their mood. The mood column is cumulative.
  - class FILMS_BLACKHOLE(BasicModel):
  - "film_id": int,
  - "film_name": str,
  - "mood1": int,
  - "mood2": int,
  - "moodi": int,
    
 





