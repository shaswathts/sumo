SIM_TIME=3600

PASS_PARAMS = -e $(SIM_TIME) -p 1 --vehicle-class passenger --trip-attributes="color=\"255,255,255\""
BUS_PARAMS = -e $(SIM_TIME) -p 30 --vehicle-class bus --trip-attributes="accel=\"0.8\""
TRUCK_PARAMS = -e $(SIM_TIME) -p 15 --vehicle-class truck --trip-attributes="color=\"179,223,183\""
TRAILER_PARAMS = -e $(SIM_TIME) -p 150 --vehicle-class trailer --trip-attributes="color=\"223,179,180\" accel=\"0.5\""
DELIVERY_PARAMS = -e $(SIM_TIME) -p 30 --vehicle-class delivery --trip-attributes="color=\"115,211,230\""

all: trips poly

poly:
	polyconvert --net-file osm.net.xml --osm-files map.osm -o reduced_map.poly.xml

trips:
	/opt/sumo-1.7.0/tools/randomTrips.py -n osm.net.xml -r bus_routes.rou.xml  -o bus_trips.xml $(BUS_PARAMS)
	/opt/sumo-1.7.0/tools/randomTrips.py -n osm.net.xml -r truck_routes.rou.xml  -o truck_trips.xml $(TRUCK_PARAMS)
	/opt/sumo-1.7.0/tools/randomTrips.py -n osm.net.xml -r delivery_routes.rou.xml  -o delivery_trips.xml $(DELIVERY_PARAMS)
	/opt/sumo-1.7.0/tools/randomTrips.py -n osm.net.xml -r passenger_routes.rou.xml  -o passenger_trips.xml $(PASS_PARAMS)
	/opt/sumo-1.7.0/tools/randomTrips.py -n osm.net.xml -r trailer_routes.rou.xml  -o trailer_trips.xml $(TRAILER_PARAMS)

	sed -i "s/vehicle id=\"/vehicle id=\"bus/g" bus_routes.rou.xml
	sed -i "s/vehicle id=\"/vehicle id=\"truck/g" truck_routes.rou.xml
	sed -i "s/vehicle id=\"/vehicle id=\"pass/g" passenger_routes.rou.xml
	sed -i "s/vehicle id=\"/vehicle id=\"deliv/g" delivery_routes.rou.xml
	sed -i "s/vehicle id=\"/vehicle id=\"trailer/g" trailer_routes.rou.xml

start:
	sumo-gui mod1.sumocfg

clean:
	rm -f *.rou.xml *.rou.alt.xml *trips.xml
	rm -f reduced_map.poly.xml
