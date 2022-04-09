import React from 'react';
import './supportresources.css';
import '../../images/AbuseAgencyResources.svg';

function SupportResources() {
  return (
    <div className="App">
      <table>
        <tr>
          <th>Agency</th>
          <th>Phone</th>
          <th>Website</th>
        </tr>
        <tr>
          <td>The National Domestic Violence Hotline </td>
          <td>1-800-799-7233 (SAFE)</td>
          <td><a href="https://www.childhelp.org/">www.childhelp.org</a></td>
        </tr>
        <tr>
          <td>National Dating Abuse Helpline </td>
          <td>1-866-331-9474</td>
          <td><a href="https://www.childhelp.org/">www.childhelp.org</a></td>
        </tr>
        <tr>
          <td>National Child Abuse Hotline/Childhelp </td>
          <td>1-800-4-A-CHILD (1-800-422-4453)</td>
          <td><a href="https://www.childhelp.org/">www.childhelp.org</a></td>
        </tr>
      </table>
    </div>
  );
}

export default SupportResources;

