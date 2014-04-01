from django import forms

from rvbd_portal.apps.datasource.forms import fields_add_time_selection
from rvbd_portal.apps.datasource.modules.analysis import AnalysisTable
from rvbd_portal.apps.datasource.models import TableField, Table, Column
from rvbd_portal.libs.fields import Function

from rvbd_portal.apps.report.models import Report, Section
from rvbd_portal.apps.report.modules import raw

from . import criteria_functions as funcs

report = Report(title='Criteria Circular Dependency')
report.save()

# Section
section = Section(report=report, title='Section 0')
section.save()

a = AnalysisTable('test-criteria-circulardependency', tables={},
                  function = funcs.analysis_echo_criteria)

TableField.create(keyword='t1', obj=a.table,
                  post_process_template='table_computed:{t2}',
                  hidden=False)

TableField.create(keyword='t2', obj=a.table,
                  post_process_template='table_computed:{t3}',
                  hidden=False)

TableField.create(keyword='t3', obj=a.table,
                  post_process_template='table_computed:{t1}',
                  hidden=False)

a.add_column('key', 'Key', iskey=True, isnumeric=False)
a.add_column('value', 'Value', isnumeric=False)

raw.TableWidget.create(section, a.table, 'Table')
