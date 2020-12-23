class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # list of destinations along route
    route = []
    # initialize cache
    cache = {}
    
    # store tickets into cache 
    for ticket in tickets:
        # source is key and desitination is value
        cache[ticket.source] = ticket.destination
    
    # add initial cached route None
    route.append(cache["NONE"])

    # traverse and stop at index of last element
    for i in range(length - 1):
        # add cached route at position of loop to result array
        route.append(cache[route[i]])

    return route

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets1 = [ticket_1, ticket_2, ticket_3]

ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets2 = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
                   ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

print(reconstruct_trip(tickets1, 3))
print(reconstruct_trip(tickets2, 10))
