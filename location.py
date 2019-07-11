def distance():
    first_city = input("Enter the first city: ")
    second_city = input("Enter the second city: ")
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="my application")
    location = geolocator.geocode(first_city)
    print(first_city, "is found in: ",location.address)
    lat = location.latitude
    long = location.longitude

    location = geolocator.geocode(second_city)
    print(second_city, "is found in: ",location.address)
    lat2 = location.latitude
    long2 = location.longitude

    from geopy.distance import geodesic
    first = (long, lat)
    second = (long2, lat2)
    print("The distance between them is",geodesic(first, second).km,"kilometers")
    
def main():
    distance()

main()