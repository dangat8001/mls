from metaflow import FlowSpec, Parameter, step, JSONType

class JSONParameterFlow(FlowSpec):
    gdp = Parameter('gdp',
                    help='Country-GDP Mapping',
                    type=JSONType,
                    default='{"US": 1939}')

    country = Parameter('country',
                        help='Chosse a country',
                        default='US')

    
    @step
    def start(self):
        print('The GDP of %s is $%dB' % (self.country, self.gdp[self.country]))
        self.next(self.end)

    @step
    def end(self):
        pass

if __name__ == '__main__':
    JSONParameterFlow()

