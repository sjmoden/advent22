class WorkOrder:
    def __init__(self, command):
        self.command = command

    def get_lower_value(self):
        return int(self.command.split('-')[0])

    def get_higher_value(self):
        return int(self.command.split('-')[1])

    def check_if_another_work_order_is_contained_in_this_work_order(self, work_order):
        if work_order.get_lower_value() >= self.get_lower_value() \
                and work_order.get_higher_value() <= self.get_higher_value():
            return True
        return False

    def check_if_another_work_order_contains_overlapping_work(self, work_order):
        if work_order.get_lower_value() <= self.get_lower_value() <= work_order.get_higher_value():
            return True
        if self.get_lower_value() <= work_order.get_lower_value() <= self.get_higher_value():
            return True
        return False
