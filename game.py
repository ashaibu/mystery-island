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


def move_player(current_location, destination, energy):
    """Move the player and reduce energy after a valid move."""

    available_moves = get_available_moves(current_location)

    if destination not in available_moves:
        return current_location, energy, False

    if energy <= 0:
        return current_location, energy, False

    new_energy = energy - 1

    return destination, new_energy, True
