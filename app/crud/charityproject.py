from typing import Optional

from sqlalchemy import extract, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(
            self,
            project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        """Функция получения ID объекта по его имени для проверки уникальности имени."""
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        return db_project_id.scalars().first()

    async def get_projects_by_completion_rate(
        self,
        session: AsyncSession,
    ) -> list[dict[str, str, str, int, str, str]]:
        """Сортирует список со всеми закрытыми проектами
        по количеству времени, которое понадобилось на сбор средств."""
        fundraising_time = (
            extract('day', CharityProject.close_date) -
            extract('day', CharityProject.create_date)
        )
        db_closed_projects = await session.execute(
            select([CharityProject.name,
                    fundraising_time.label('fundraising_time'),
                    CharityProject.description]).where(
                        CharityProject.fully_invested == 1
            ).order_by(fundraising_time)
        )
        db_closed_projects = db_closed_projects.all()
        return db_closed_projects


project_crud = CRUDCharityProject(CharityProject)
