import React, { Component } from 'react';
import { Navbar, NavItem, Nav } from 'react-bootstrap';

class Header extends Component {
  render() {
    return (
        <Navbar>
        <Navbar.Header>
          <Navbar.Brand>
            <a href="/">GS Map the Collections</a>
          </Navbar.Brand>
        </Navbar.Header>
        <Nav>
          <NavItem eventKey={1} href="/data">
            Data
          </NavItem>
          <NavItem eventKey={2} href="/visualize">
            Visualize
          </NavItem>
          <NavItem eventKey={3} href="/search">
            Search
          </NavItem>
        </Nav>
      </Navbar>
    );
  }
}

export default Header;
