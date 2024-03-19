from modules import parking_lot

def describe_parking_lot():
    def should_create_a_valid_parking_lot():
        """🧪 expect """
        garage = parking_lot.Garage(1, 7, [4])
        assert garage.levelLength == 7 and garage.stairsIndexes == [4]

    def should_return_None_on_out_of_bound_parking_index():
        """ expect input position 8 to return None"""
        garage = parking_lot.Garage(1, 7, [4])
        assert garage.route(0, 8) == None

    def should_return_7left_on_parking_index_7():
        """ expect input position 7 to return 7 left"""
        garage = parking_lot.Garage(1, 7, [4])
        assert garage.route(0, 7) == ["7 left"]

    def walking_route_ground_floor_from_index_0():
        """ expect You are on the exit when at the exit"""
        garage = parking_lot.Garage(1, 7, [4])
        assert garage.route(0, 0) == ["You are on the exit"]

    def walking_route_first_floor_from_index_1():
        """ expect walking route to the exit"""
        garage = parking_lot.Garage(2, 7, [4])
        assert garage.route(1, 1) == ["3 left","1 down","5 right"]


        
