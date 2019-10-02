from graphene import String, Int, Boolean, Float,\
    Field, List, ObjectType, NonNull


class Cores(ObjectType):
    core_serial = String()
    flight = Int()
    gridfins = Boolean()
    legs = Boolean()
    reused = Boolean()
    landing_intent = Boolean()
    landing_type = String()
    block = Int()
    land_success = Boolean()
    landing_vehicle = String()


class First_Stage_Type(ObjectType):
    cores = List(NonNull(Cores))


class Orbit_Params(ObjectType):
    reference_system = NonNull(String)
    regime = NonNull(String)
    longitude = Float()
    semi_major_axis_km = NonNull(Float)
    eccentricity = NonNull(Float)
    periapsis_km = NonNull(Float)
    apoapsis_km = NonNull(Float)
    inclination_deg = NonNull(Float)
    period_min = NonNull(Float)
    lifespan_years = Int()
    epoch = NonNull(String)
    mean_motion = NonNull(Float)
    raan = NonNull(Float)
    arg_of_pericenter = NonNull(Float)
    mean_anomaly = NonNull(Float)


class Payload(ObjectType):
    payload_id = NonNull(String)
    reused = NonNull(Boolean)
    nationality = NonNull(String)
    manufacturer = NonNull(String)
    payload_type = NonNull(String)
    payload_mass_kg = NonNull(Int)
    payload_mass_lbs = NonNull(Int)
    orbit = NonNull(String)
    orbit_params = NonNull(Orbit_Params)
    customers = List(NonNull(String))
    norad_id = List(Int)


class Second_Stage_Type(ObjectType):
    block = Int()
    payload = List(NonNull(Payload))


class Fairings(ObjectType):
    reused = NonNull(Boolean)
    recovery_attempt = Boolean()
    recovered = Boolean()
    ship = String()


class Rocket_Type(ObjectType):
    rocket_id = NonNull(String)
    rocket_name = NonNull(String)
    rocket_type = NonNull(String)
    first_stage = NonNull(First_Stage_Type)
    second_stage = NonNull(Second_Stage_Type)
    fairings = Field(Fairings)


class Telemetry(ObjectType):
    flight_club = String()


class Launch_Site(ObjectType):
    site_id = NonNull(String)
    site_name = NonNull(String)
    site_name_long = NonNull(String)


class Links(ObjectType):
    mission_patch = String()
    reddit_campaign = String()
    reddit_launch = String()
    reddit_recovery = String()
    reddit_media = String()
    presskit = String()
    article_link = String()
    wikipedia = String()
    video_link = String()
    flickr_images = List(NonNull(String))


class Timeline(ObjectType):
    webcast_liftoff = Int()
    go_for_prop_loading = Int()
    rp1_loading = Int()
    stage1_lox_loading = Int()
    stage2_lox_loading = Int()
    engine_chill = Int()
    prelaunch_checks = Int()
    propellant_pressurization = Int()
    go_for_launch = Int()
    ignition = Int()
    liftoff = Int()
    maxq = Int()
    meco = Int()
    stage_sep = Int()
    second_stage_ignition = Int()
    fairing_deploy = Int()
    # seco-1 = Int()
    payload_deploy_1 = Int()
    second_stage_restart = Int()
    # seco-2 = Int()
    payload_deploy_2 = Int()


class All_Launches(ObjectType):
    flight_number = NonNull(Int)
    mission_name = NonNull(String)
    upcoming = NonNull(Boolean)
    launch_year = NonNull(String)
    launch_date_unix = NonNull(Int)
    is_tentative = NonNull(Boolean)
    tentative_max_precision = NonNull(String)
    tbd = NonNull(Boolean)
    rocket = NonNull(Rocket_Type)
    mission_id = List(String)
    launch_window = Int()
    ships = List(NonNull(String))
    telemetry = NonNull(Telemetry)
    launch_site = NonNull(Launch_Site)
    launch_success = Boolean()
    links = NonNull(Links)
    details = String()
    upcoming = NonNull(Boolean)
    static_fire_date_unix = Int()
    timeline = Field(Timeline)
    # crew = List()
