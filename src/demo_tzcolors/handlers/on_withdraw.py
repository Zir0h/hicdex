import demo_tzcolors.models as models
from demo_tzcolors.types.tzcolors_auction.parameter.withdraw import Withdraw
from dipdup.models import HandlerContext, OperationContext


async def on_withdraw(
    ctx: HandlerContext,
    withdraw: OperationContext[Withdraw],
) -> None:
    auction = await models.Auction.filter(
        id=withdraw.parameter.__root__,
    ).get()

    # FIXME: Don't do that, returns None when id=0. Bug in Tortoise?
    # token = await auction.token
    token = await models.Token.filter(id=auction.token_id).get()  # type: ignore

    token.holder = await auction.bidder
    await token.save()

    auction.status = models.AuctionStatus.FINISHED
    await auction.save()