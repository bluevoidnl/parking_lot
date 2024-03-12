from modules import parking_lot

def describe_parking_lot():
    def should_create_a_valid_parking_lot():
        """🧪 expect """
        garage = parking_lot.Garage(7, [4])
        assert garage.levelLength == 7 and garage.stairsIndexes == [4]

    def should_return_None_on_out_of_bound_parking_index():
        """ expect input position 8 to return None"""
        garage = parking_lot.Garage(7, [4])
        assert garage.route(0, 8) == None

    def should_return_7left_on_parking_index_7():
        """ expect input position 7 to return """
        garage = parking_lot.Garage(7, [4])
        assert garage.route(0, 7) == ["7 left"]
