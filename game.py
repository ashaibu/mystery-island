
# Locations connected to each other
ISLAND_PATHS = {
    "Beach": ["Jungle"],
    "Jungle": ["Beach", "Cave"],
    "Cave": ["Jungle", "Old Bridge"],
    "Old Bridge": ["Cave", "Lighthouse"],
    "Lighthouse": ["Old Bridge"]
}


def get_available_moves(location):
    """Return the locations connected to the current location."""
    return ISLAND_PATHS.get(location, [])
