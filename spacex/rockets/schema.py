from graphene import ObjectType, List, NonNull,\
    String, Int, Float, Boolean


class Payload_Weights(ObjectType):
    id = NonNull(String)
    name = NonNull(String)
    kg = NonNull(Int)


class Height(ObjectType):
    meters = NonNull(Int)


class Diameter(ObjectType):
    meters = NonNull(Float)


class Mass(ObjectType):
    kg = NonNull(Int)


class Thrust_Sea_Level(ObjectType):
    kN = NonNull(Int)


class Thrust_Vacuum(ObjectType):
    kN = NonNull(Int)


class First_Stage(ObjectType):
    reusable = NonNull(Boolean)
    engines = NonNull(Int)
    fuel_amount_tons = NonNull(Int)
    burn_time_sec = NonNull(Int)
    thrust_sea_level = NonNull(Thrust_Sea_Level)
    thrust_vacuum = NonNull(Thrust_Vacuum)


class Thrust(ObjectType):
    kN = NonNull(Int)


class Composite_Fairing(ObjectType):
    height = NonNull(Height)
    diameter = NonNull(Diameter)


class Payloads(ObjectType):
    option_1 = NonNull(String)
    option_2 = NonNull(String)
    composite_fairing = NonNull(Composite_Fairing)


class Second_Stage(ObjectType):
    engines = NonNull(Int)
    fuel_amount_tons = NonNull(Int)
    burn_time_sec = NonNull(Int)
    thrust = NonNull(Thrust)
    payloads = NonNull(Payloads)


class Engines(ObjectType):
    number = NonNull(Int)
    type = NonNull(String)
    version = NonNull(String)
    layout = NonNull(String)
    engine_loss_max = NonNull(Int)
    propellant_1 = NonNull(String)
    propellant_2 = NonNull(String)
    thrust_sea_level = NonNull(Thrust_Sea_Level)
    thrust_vacuum = NonNull(Thrust_Vacuum)
    thrust_to_weight = NonNull(Float)


class Landing_Legs(ObjectType):
    number = NonNull(Int)
    material = String()


class Rocket(ObjectType):
    id = NonNull(Int)
    active = NonNull(Boolean)
    stages = NonNull(Int)
    boosters = NonNull(Int)
    cost_per_launch = NonNull(Int)
    success_rate_pct = NonNull(Int)
    first_flight = NonNull(String)
    country = NonNull(String)
    company = NonNull(String)
    height = NonNull(Height)
    diameter = NonNull(Diameter)
    mass = NonNull(Mass)
    payload_weights = List(NonNull(Payload_Weights))
    first_stage = NonNull(First_Stage)
    second_stage = NonNull(Second_Stage)
    engines = NonNull(Engines)
    landing_legs = NonNull(Landing_Legs)
    wikipedia = NonNull(String)
    description = NonNull(String)
    rocket_id = NonNull(String)
    rocket_name = NonNull(String)
    rocket_type = NonNull(String)
