import React, { Component } from 'react';
import { Navbar, NavItem, Nav } from 'react-bootstrap';

class Header extends Component {
  render() {
    return (
        <Navbar>
        <Navbar.Header>
          <Navbar.Brand>
            <a href="#home">GS Map the Collections</a>
          </Navbar.Brand>
        </Navbar.Header>
        <Nav>
          <NavItem eventKey={1} href="#">
            Data
          </NavItem>
          <NavItem eventKey={2} href="#">
            Visualize
          </NavItem>
        </Nav>
      </Navbar>
    );
  }
}

export default Header;
