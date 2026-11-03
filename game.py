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


def move_player(current_location, destination, energy, inventory):
    """Move the player if the destination is valid and requirements are met."""

    available_moves = get_available_moves(current_location)

    if destination not in available_moves:
        return current_location, energy, False

    if energy <= 0:
        return current_location, energy, False

    if destination == "Old Bridge" and "Rope" not in inventory:
        return current_location, energy, False

    if destination == "Lighthouse" and "Lantern" not in inventory:
        return current_location, energy, False

    new_energy = energy - 1

    return destination, new_energy, True

# Items found at different island locations
LOCATION_ITEMS = {
    "Jungle": "Rope",
    "Cave": "Lantern"
}


def collect_item(location, inventory):
    """Automatically collect an item when entering its location."""

    item = LOCATION_ITEMS.get(location)

    if item is not None and item not in inventory:
        inventory.append(item)
        return item

    return None

