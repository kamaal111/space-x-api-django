import graphene
import requests
import graphql

from config import spacex_api_url


class Cores(graphene.ObjectType):
    core_serial = graphene.String()
    flight = graphene.Int()
    gridfins = graphene.Boolean()
    legs = graphene.Boolean()
    reused = graphene.Boolean()
    landing_intent = graphene.Boolean()
    landing_type = graphene.String()
    block = graphene.Int()
    land_success = graphene.Boolean()
    landing_vehicle = graphene.String()


class First_Launch(graphene.ObjectType):
    cores = graphene.List(graphene.NonNull(Cores))


class Orbit_Params(graphene.ObjectType):
    reference_system = graphene.NonNull(graphene.String)
    regime = graphene.NonNull(graphene.String)
    longitude = graphene.Float()
    semi_major_axis_km = graphene.NonNull(graphene.Float)
    eccentricity = graphene.NonNull(graphene.Float)
    periapsis_km = graphene.NonNull(graphene.Float)
    apoapsis_km = graphene.NonNull(graphene.Float)
    inclination_deg = graphene.NonNull(graphene.Float)
    period_min = graphene.NonNull(graphene.Float)
    lifespan_years = graphene.Int()
    epoch = graphene.NonNull(graphene.String)
    mean_motion = graphene.NonNull(graphene.Float)
    raan = graphene.NonNull(graphene.Float)
    arg_of_pericenter = graphene.NonNull(graphene.Float)
    mean_anomaly = graphene.NonNull(graphene.Float)


class Payload(graphene.ObjectType):
    payload_id = graphene.NonNull(graphene.String)
    reused = graphene.NonNull(graphene.Boolean)
    nationality = graphene.NonNull(graphene.String)
    manufacturer = graphene.NonNull(graphene.String)
    payload_type = graphene.NonNull(graphene.String)
    payload_mass_kg = graphene.NonNull(graphene.Int)
    payload_mass_lbs = graphene.NonNull(graphene.Int)
    orbit = graphene.NonNull(graphene.String)
    orbit_params = graphene.NonNull(Orbit_Params)
    customers = graphene.List(graphene.NonNull(graphene.String))
    norad_id = graphene.List(graphene.Int)


class Second_Launches(graphene.ObjectType):
    block = graphene.Int()
    payload = graphene.List(graphene.NonNull(Payload))


class Fairings(graphene.ObjectType):
    reused = graphene.Boolean()
    recovery_attempt = graphene.Boolean()
    recovered = graphene.Boolean()
    ship = graphene.String()


class Rocket(graphene.ObjectType):
    rocket_id = graphene.NonNull(graphene.String)
    rocket_name = graphene.NonNull(graphene.String)
    rocket_type = graphene.NonNull(graphene.String)
    first_stage = graphene.NonNull(First_Launch)
    second_stage = graphene.NonNull(Second_Launches)
    fairings = graphene.Field(Fairings)


class Telemetry(graphene.ObjectType):
    flight_club = graphene.String()


class Launch_Site(graphene.ObjectType):
    site_id = graphene.NonNull(graphene.String)
    site_name = graphene.NonNull(graphene.String)
    site_name_long = graphene.NonNull(graphene.String)


class Links(graphene.ObjectType):
    mission_patch = graphene.String()
    reddit_campaign = graphene.String()
    reddit_launch = graphene.String()
    reddit_recovery = graphene.String()
    reddit_media = graphene.String()
    presskit = graphene.String()
    article_link = graphene.String()
    wikipedia = graphene.String()
    video_link = graphene.String()
    flickr_images = graphene.List(graphene.NonNull(graphene.String))


class Timeline(graphene.ObjectType):
    webcast_liftoff = graphene.Int()
    go_for_prop_loading = graphene.Int()
    rp1_loading = graphene.Int()
    stage1_lox_loading = graphene.Int()
    stage2_lox_loading = graphene.Int()
    engine_chill = graphene.Int()
    prelaunch_checks = graphene.Int()
    propellant_pressurization = graphene.Int()
    go_for_launch = graphene.Int()
    ignition = graphene.Int()
    liftoff = graphene.Int()
    maxq = graphene.Int()
    meco = graphene.Int()
    stage_sep = graphene.Int()
    second_stage_ignition = graphene.Int()
    fairing_deploy = graphene.Int()
    # seco-1 = graphene.Int()
    payload_deploy_1 = graphene.Int()
    second_stage_restart = graphene.Int()
    # seco-2 = graphene.Int()
    payload_deploy_2 = graphene.Int()


class Launch(graphene.ObjectType):
    flight_number = graphene.NonNull(graphene.Int)
    mission_name = graphene.NonNull(graphene.String)
    upcoming = graphene.NonNull(graphene.Boolean)
    launch_year = graphene.NonNull(graphene.String)
    launch_date_unix = graphene.NonNull(graphene.Int)
    is_tentative = graphene.NonNull(graphene.Boolean)
    tentative_max_precision = graphene.NonNull(graphene.String)
    tbd = graphene.NonNull(graphene.Boolean)
    rocket = graphene.NonNull(Rocket)
    mission_id = graphene.List(graphene.String)
    launch_window = graphene.Int()
    ships = graphene.List(graphene.NonNull(graphene.String))
    telemetry = graphene.NonNull(Telemetry)
    launch_site = graphene.NonNull(Launch_Site)
    launch_success = graphene.Boolean()
    links = graphene.NonNull(Links)
    details = graphene.String()
    upcoming = graphene.NonNull(graphene.Boolean)
    static_fire_date_unix = graphene.Int()
    timeline = graphene.Field(Timeline)
    # crew = graphene.List()
