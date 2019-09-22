{
allLaunches {
flightNumber
missionName
upcoming
launchYear
launchDateUnix
isTentative
tentativeMaxPrecision
tbd
missionId
launchWindow
ships
launchSuccess
details
upcoming
staticFireDateUnix

# crew

    rocket {
      rocketId
      rocketName
      rocketType
      firstStage {
        cores {
          coreSerial
          flight
          gridfins
          legs
          reused
          landingIntent
          landingType
          block
          landSuccess
          landingVehicle
        }
      }
      secondStage {
        block
        payload {
          payloadId
          reused
          nationality
          manufacturer
          payloadType
          payloadMassKg
          payloadMassLbs
          orbit
          customers
          noradId
          orbitParams {
            referenceSystem
            regime
            longitude
            semiMajorAxisKm
            eccentricity
            periapsisKm
            apoapsisKm
            inclinationDeg
            periodMin
            lifespanYears
            epoch
            meanMotion
            raan
            argOfPericenter
            meanAnomaly
          }
        }
      }
      fairings {
        reused
      }
    }
    telemetry {
        flightClub
    }
    launchSite {
      siteId
      siteName
      siteNameLong
    }
    links {
      missionPatch
      redditCampaign
      redditLaunch
      redditRecovery
      redditMedia
      presskit
      articleLink
      redditMedia
      presskit
      articleLink
      wikipedia
      videoLink
      flickrImages
    }
    timeline {
      webcastLiftoff
      goForPropLoading
      rp1Loading
      stage1LoxLoading
      stage2LoxLoading
      engineChill
      prelaunchChecks
      propellantPressurization
      goForLaunch
      ignition
      liftoff
      maxq
      meco
      stageSep
      secondStageIgnition
      fairingDeploy

# seco1

      payloadDeploy1
      secondStageRestart

# seco2

      payloadDeploy2
    }

}
}
