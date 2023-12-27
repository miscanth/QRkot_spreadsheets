from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import extract, select

from app.models import CharityProject


async def get_fundraising_time(
        project: CharityProject,
        session: AsyncSession,
):
    """Функция вычисления времени, которое понадобилось
    на сбор средств для закрытого проекта."""
    time_for_raising = await session.execute(
        select(extract('day', project.close_date) - extract('day', project.create_date))
    )
    return time_for_raising.scalars().first()
