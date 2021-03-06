from dataclasses import dataclass


@dataclass
class PayloadModelBase:
    state_code: str = None
    start_date: str = None
    end_date: str = None
    pagination_start: int = 0

    # fetch_all = True

    def payload(self):
        # just intercept the payload calls so they aren't relayed to `object`
        pass
