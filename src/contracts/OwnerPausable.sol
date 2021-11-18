// SPDX-License-Identifier: GPL-3.0-or-later
pragma solidity 0.6.9;

import { PausableUpgradeable } from "@openzeppelin/contracts-ethereum-package-upgradeable/contracts/utils/PausableUpgradeable.sol";
import { PerpFiOwnableUpgrade } from "../utils/PerpFiOwnableUpgrade.sol";

contract OwnerPausableUpgradeSafe is PerpFiOwnableUpgrade, PausableUpgradeable {
    // solhint-disable func-name-mixedcase
    function __OwnerPausable_init() internal initializer {
        __Ownable_init();
        __Pausable_init();
    }

    function pause() public onlyOwner {
        _pause();
    }

    function unpause() public onlyOwner {
        _unpause();
    }

    uint256[50] private __gap;
}
